## 0.7.4 (2024-07-01)

### Fix

- add dynamo permision

## 0.7.3 (2024-07-01)

### Fix

- ruff version

## 0.7.2 (2024-06-26)

### Fix

- move sqs to utils

## 0.7.1 (2024-06-12)

### Fix

- topic subscription method

## 0.7.0 (2024-06-12)

### Feat

- added sns sqs integration

## 0.6.4 (2024-06-12)

### Fix

- increased concurrency

## 0.6.3 (2024-06-10)

### Fix

-  max batch size incrise

## 0.6.2 (2024-06-04)

### Fix

- the rule uses the stage

## 0.6.1 (2024-06-04)

### Fix

- the return for functions is a queue

## 0.6.0 (2024-06-04)

### Feat

- added sqs eventbridge helper target

## 0.5.4 (2024-06-04)

### Fix

- now it returns the queue when created

## 0.5.3 (2024-06-04)

### Fix

- max batching

## 0.5.2 (2024-06-04)

### Fix

- changed defaults for queues

## 0.5.1 (2024-05-28)

### Fix

- now addqueue uses func name

## 0.5.0 (2024-05-28)

### Feat

- added sqs per lambda creation

## 0.4.17 (2024-05-28)

### Fix

- remove cfn output for functions

## 0.4.16 (2024-05-28)

### Fix

- dlq spelling

## 0.4.15 (2024-05-28)

### Fix

- monitoring spelling

## 0.4.14 (2024-05-28)

### Fix

- added functions property

## 0.4.13 (2024-05-27)

### Fix

- added dlq and logging for factory

## 0.4.12 (2024-05-23)

### Fix

- datadog inject_log

## 0.4.11 (2024-05-23)

### Fix

- changed logging to json fix

## 0.4.10 (2024-05-23)

### Fix

- changed logging to json

## 0.4.9 (2024-05-23)

### Fix

- changed memory size

## 0.4.8 (2024-05-23)

### Fix

- remove reserved concurrent

## 0.4.7 (2024-05-23)

### Fix

- decrease the reserved concurrency

## 0.4.6 (2024-05-23)

### Fix

- retry attemps should be 2

## 0.4.5 (2024-05-23)

### Fix

- change reserved concurrency

## 0.4.4 (2024-05-23)

### Fix

- added autoscale

## 0.4.3 (2024-05-22)

### Fix

- added cloudwatch role to apigw

## 0.4.2 (2024-05-21)

### Fix

- make scope optional for apigw

## 0.4.1 (2024-05-21)

### Fix

- added optional scope

## 0.4.0 (2024-05-21)

### Feat

- added sqs integration to the apigw factory

## 0.3.17 (2024-05-20)

### Fix

- changed the name of the env variable

## 0.3.16 (2024-05-17)

### Fix

- changed so the output uses the scope

## 0.3.15 (2024-05-17)

### Fix

- remove cfn output

## 0.3.14 (2024-05-17)

### Fix

- export_name again

## 0.3.13 (2024-05-17)

### Fix

- export_name

## 0.3.12 (2024-05-17)

### Fix

- sevice -> service

## 0.3.11 (2024-05-16)

### Fix

- added service name to dd

## 0.3.10 (2024-05-16)

### Fix

- remove print

## 0.3.9 (2024-05-16)

### Fix

- print function name on creation

## 0.3.8 (2024-05-16)

### Fix

- add function list

## 0.3.7 (2024-05-16)

### Fix

- update dependecies

## 0.3.6 (2024-05-16)

### Fix

- the name formater now uses underscores

## 0.3.5 (2024-05-15)

### Fix

- make folder if it doesn't exists again

## 0.3.4 (2024-05-15)

### Fix

- make folder if it doesn't exists

## 0.3.3 (2024-05-15)

### Fix

- datadog site fix

## 0.3.2 (2024-05-15)

### Fix

- constructs version

## 0.3.1 (2024-05-15)

### Fix

- datadog factory init

## 0.3.0 (2024-05-15)

### Feat

- layer now is build to site-packages

## 0.2.14 (2024-05-13)

### Fix

- added dynamo to default policies

## 0.2.13 (2024-05-11)

### Fix

- **apigw**: the path can be empty now for sure

## 0.2.12 (2024-05-11)

### Fix

- **lambda**: default policy now has a resource

## 0.2.11 (2024-05-11)

### Fix

- **apigw**: the path can be empty

## 0.2.10 (2024-05-11)

### Fix

- prefix can be empty

## 0.2.9 (2024-05-11)

### Fix

- more relative import

## 0.2.8 (2024-05-11)

### Fix

- added relative import

## 0.2.7 (2024-05-11)

### Fix

- remove partial import

## 0.2.6 (2024-05-11)

### Fix

- rename to folder containing package

## 0.2.5 (2024-05-11)

### Fix

- change to __init__

## 0.2.4 (2024-05-11)

### Fix

- module packaging again

## 0.2.3 (2024-05-11)

### Fix

- module packaging again

## 0.2.3 (2024-05-11)

### Fix

- module packaging again

## 0.2.2 (2024-05-11)

### Fix

- module packaging

## 0.2.1 (2024-05-11)

### Fix

- module name

## 0.2.0 (2024-05-11)

### Feat

- added apigateway factory

### Fix

- added output for when functions are created

## 0.1.0 (2024-05-10)

### Feat

- added datadog construct for python monitoring
- added factory for python lambdas
- added dependecies and the base factory
- commit config
