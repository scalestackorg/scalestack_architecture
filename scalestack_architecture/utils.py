from aws_cdk.aws_events import Rule, EventBus
from aws_cdk.aws_events_targets import SqsQueue
from aws_cdk.aws_sqs import Queue


def create_event_bridge_sqs_target(
    event_bus: EventBus, queue: Queue, rule_name: str, event_pattern: dict
):
    """
    Create an EventBridge rule that sends events to an SQS queue
    :param event_bus: The EventBridge event bus
    :param queue: The SQS queue
    :param rule_name: The name of the rule
    :param event_pattern: The event pattern to match
    :return: Rule
    """
    return Rule(
        queue.stack,
        rule_name,
        rule_name=rule_name,
        event_bus=event_bus,
        targets=[SqsQueue(queue)],
        event_pattern=event_pattern,
    )
