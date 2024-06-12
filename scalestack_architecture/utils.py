from aws_cdk.aws_events import Rule, EventBus
from aws_cdk.aws_events_targets import SqsQueue
from aws_cdk.aws_sqs import Queue
from aws_cdk.aws_sns import Topic
from aws_cdk.aws_sns_subscriptions import SqsSubscription


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
    :return: Subscription
    """
    return SqsSubscription(
        queue,
        raw_message_delivery=True,
        topic=topic,
        filter_policy_with_message_body=filter_policy,
    )
