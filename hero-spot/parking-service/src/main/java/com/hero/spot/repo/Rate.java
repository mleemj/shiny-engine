package com.hero.spot.repo;

/**
 * Rate entity data object
 * 
 */
public class Rate {
	private String days;
	private String times;
	private Integer price;

	public String getDays() {
		return days;
	}

	public void setDays(String days) {
		this.days = days;
	}

	public String getTimes() {
		return times;
	}

	public void setTimes(String times) {
		this.times = times;
	}

	public Integer getPrice() {
		return price;
	}

	public void setPrice(Integer price) {
		this.price = price;
	}

	@Override
	public String toString() {
		StringBuilder sbldr = new StringBuilder();
		sbldr.append("days: " + days).append(" times: " + times).append(" price: " + price);
		return sbldr.toString();
	}
}
