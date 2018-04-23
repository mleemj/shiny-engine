package com.hero.spot.repo;

import java.util.List;
import java.util.logging.Logger;

import com.hero.spot.domain.Facility;

public class RateRepo {
	private Logger logger = Logger.getLogger(RateRepo.class.getName());
	private Facility ohare;

	public Facility getFacility() {
		RateInterface datasource = RateDatasource.getInstance().getDatasource();
		List<Rate> rates = datasource.getRates();
		if (ohare == null) {
			RateParser parser = new RateParser();
			ohare = parser.parseRate(rates);
		}
		return ohare;
	}
}
