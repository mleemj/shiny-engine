package com.hero.spot.repo;

import java.util.List;

public class OhareRate implements RateInterface{
	private List<Rate> rates;

	public List<Rate> getRates() {
		return rates;
	}

	public void setRates(List<Rate> rates) {
		this.rates = rates;
	}

	@Override
	public String toString() {
		StringBuilder sbldr = new StringBuilder();
		rates.forEach((Rate r) -> sbldr.append(r.toString()));
		return sbldr.toString();
	}
}
