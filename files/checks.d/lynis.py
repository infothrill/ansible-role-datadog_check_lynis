# -*- coding: utf-8 -*-
"""
Datadog check for Lynis (https://cisofy.com/lynis/)

This will query the Lynis report for numeral data and feed it into datadog.
"""

from checks import AgentCheck

METRIC_PREFIX = "lynis."

class LynisCheck(AgentCheck):

    KNOWN_METRICS = ("hardening_index", "lynis_tests_done", "installed_packages")
    def get_metrics_from_report(self, report):
        metrics = []
        with open(report, "r") as f:
            for line in f:
                if not line.startswith("#"):
                    key, _, value = line.partition("=")
                    if key in self.KNOWN_METRICS:
                        metrics.append(tuple([key, value]))
        return metrics

    def _get_config(self, instance):
        tags = instance.get('tags', [])
        metrics = instance.get('metrics', [])
        report = instance.get('report', "/var/log/lynis-report.dat")

        instance_config = {
            'tags': tags,
            'metrics': metrics,
            'report': report
        }
        return instance_config

    def check(self, instance):
        config = self._get_config(instance)
        report = config['report']
        tags = config['tags']
        metrics = config['metrics']
        for metric in self.get_metrics_from_report(report):
            if len(metrics) == 0 or metric[0] in metrics:
                self.log.debug('lynis.{}:{}'.format(metric[0], metric[1]))
                self.gauge(METRIC_PREFIX + metric[0], float(metric[1]), tags=tags)


if __name__ == '__main__':
    check, instances = LynisCheck.from_yaml('/etc/dd-agent/conf.d/lynis.yaml')
    for instance in instances:
        print "\nRunning the check with: %r" % (instance)
        check.check(instance)
        if check.has_events():
            print 'Events: %s' % (check.get_events())
        print 'Metrics: %s' % (check.get_metrics())
