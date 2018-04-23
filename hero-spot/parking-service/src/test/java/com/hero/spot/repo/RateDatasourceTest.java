package com.hero.spot.repo;

import static org.junit.Assert.assertNotNull;

import java.util.List;
import java.util.logging.Logger;

import org.junit.Test;

public class RateDatasourceTest {
	private Logger logger = Logger.getLogger(RateDatasourceTest.class.getName());

	@Test
	public void test() {
		RateInterface rates = RateDatasource.getInstance().getDatasource();
		List<Rate> allrates = rates.getRates();
		allrates.forEach((Rate r) -> logger.info(r.getTimes()));
		assertNotNull(allrates);
	}

}
