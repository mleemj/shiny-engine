package com.hero.spot;

import com.codahale.metrics.Histogram;
import com.codahale.metrics.MetricRegistry;
import com.codahale.metrics.servlets.MetricsServlet;

/**
 * Provide general metrics. Servlet mapping in web.xml
 * 
 * mvn clean compile jetty:run
 * curl http://localhost:8080/parking-service/metrics
 *
 */
public class MyMetricsServletContextListener extends MetricsServlet.ContextListener {
  private static MetricRegistry METRIC_REGISTRY
   = new MetricRegistry();

  static {
      com.codahale.metrics.Counter counter = METRIC_REGISTRY.counter("m01-counter");
      counter.inc();

      Histogram histogram = METRIC_REGISTRY.histogram("m02-histogram");
      histogram.update(5);
      histogram.update(20);
      histogram.update(100);
  }

  public MetricRegistry getMetricRegistry() {
      return METRIC_REGISTRY;
  }
}