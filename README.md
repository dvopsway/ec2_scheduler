# ec2_scheduler

Wanna schedule stop and start of ec2 instances(like development machines) during night times.

## Installation :

Use pip to install ec2_scheduler

```
pip install ec2_scheduler
```

#### Alternate installation

You can also compile from source, just clone the repo and run the command below:

```
python setup.py install
```

## Getting Started :

You need to pass access key & secret key to ec2_scheduler.

Tip : create a seperate user account with only rights of describing, stopping and starting instances. IAM policy for that is below:
```
{
        "Statement": [
                {
                  "Action": [
				    "ec2:DescribeInstances",
                    "ec2:StartInstances",
                    "ec2:StopInstances"
				  ], 
                  "Effect": "Allow", 
                  "Resource": "*"
                }
              ]
}
```

To get started, start with --help
```
➜  ec2_scheduler --help
Usage: ec2_scheduler [OPTIONS]

Options:
  -a, --access_key TEXT  Enter AWS access key
  -s, --secret_key TEXT  Enter AWS secret key
  --help                 Show this message and exit.
```

Add following tags to your instances you wanna autoschedule:

- auto:stop : value should be a cron like : 0 1 * * * ; i.e stop at 1 am everyday 
- auto:start : value should be a cron like : 0 8 * * * ; i.e start at 8 am everyday 

Check the example usage to get started

## Example Usage :

```
➜  ec2_scheduler --access_key "xxxxxxxxxxxxxxxxx" --secret_key "xxxxxxxxxxxxxxxxx"
```

## Credits :

Based on Shing Chen Article [Auto Start and Stop Your EC2 Instances](https://schen1628.wordpress.com/2014/02/04/auto-start-and-stop-your-ec2-instances/)
