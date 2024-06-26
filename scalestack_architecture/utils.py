from aws_cdk.aws_events import Rule, EventBus
from aws_cdk.aws_events_targets import SqsQueue
from aws_cdk.aws_sqs import Queue
from aws_cdk.aws_sns import Topic
from aws_cdk.aws_sns_subscriptions import SqsSubscription
import aws_cdk.aws_lambda as lambda_
from aws_cdk import Duration
from aws_cdk.aws_lambda_event_sources import SqsEventSource


def create_event_bridge_sqs_target(
    event_bus: EventBus, queue: Queue, rule_name: str, event_pattern: dict, stage: str
):
    """
    Create an EventBridge rule that sends events to an SQS queue
    :param event_bus: The EventBridge event bus
    :param queue: The SQS queue
    :param rule_name: The name of the rule
    :param event_pattern: The event pattern to match
    :param stage: The stage of the stack (e.g. dev, prod)
    :return: Rule
    """
    rule_name = f"{stage}_{rule_name}"
    return Rule(
        queue.stack,
        rule_name,
        rule_name=rule_name,
        event_bus=event_bus,
        targets=[SqsQueue(queue)],
        event_pattern=event_pattern,
    )


def create_sns_to_sqs_subscription(
    topic: Topic, queue: Queue, filter_policy: dict = None
):
    """
    Create an SNS subscription to an SQS queue
    :param topic: The SNS topic
    :param queue: The SQS queue
    """
    subs = SqsSubscription(
        queue,
        raw_message_delivery=True,
        filter_policy_with_message_body=filter_policy,
    )
    topic.add_subscription(subs)


def add_queue_to_lambda(
    self,
    func: lambda_.Function,
    function_name: str,
    batch_size: int = 30,
    max_concurrency: int = 30,
    visibility_timeout: int = 900,
    max_batching_window: int = 5,
):
    """
    Add an SQS queue as an event source to a Lambda function
    :param func: The Lambda function
    :param batch_size: The number of messages to process in a batch (default 30)
    :param max_concurrency: The maximum number of concurrent executions (default 30)
    :param visibility_timeout: The visibility timeout of the messages in seconds (default 900)
    :param max_batching_window: The maximum time to wait for messages to arrive in seconds (default 5)
    """
    queue = Queue(
        self.stack,
        function_name + "-queue",
        queue_name=function_name + "-queue",
        visibility_timeout=Duration.seconds(visibility_timeout),
    )
    queue.grant_send_messages(func)
    queue.grant_consume_messages(func)
    func.add_event_source(
        SqsEventSource(
            queue,
            batch_size=batch_size,
            max_concurrency=max_concurrency,
            max_batching_window=(
                Duration.seconds(max_batching_window) if max_batching_window else None
            ),
            report_batch_item_failures=True,
        )
    )
    return queue
