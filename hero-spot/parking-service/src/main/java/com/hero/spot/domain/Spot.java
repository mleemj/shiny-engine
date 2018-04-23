package com.hero.spot.domain;

import java.time.DayOfWeek;
import java.time.LocalTime;

import org.apache.commons.lang3.builder.HashCodeBuilder;

public class Spot {
	private DayOfWeek dayOfWeek;
	private LocalTime hourOfDay;
	private LocalTime startTime;
	private LocalTime endTime;
	private Integer price;

	public DayOfWeek getDayOfWeek() {
		return dayOfWeek;
	}

	public void setDayOfWeek(DayOfWeek dayOfWeek) {
		this.dayOfWeek = dayOfWeek;
	}

	public LocalTime getStartTime() {
		return startTime;
	}

	public void setStartTime(LocalTime startTime) {
		this.startTime = startTime;
	}

	public LocalTime getEndTime() {
		return endTime;
	}

	public void setEndTime(LocalTime endTime) {
		this.endTime = endTime;
	}

	public Integer getPrice() {
		return price;
	}

	public void setPrice(Integer price) {
		this.price = price;
	}

	public LocalTime getHourOfDay() {
		return hourOfDay;
	}

	public void setHourOfDay(LocalTime hourOfDay) {
		this.hourOfDay = hourOfDay;
	}
	
	@Override
	public boolean equals(Object o ) {
		if (!( o instanceof Spot)) return false;
		Spot otherSpot = (Spot) o;
		boolean isEqual = this.getDayOfWeek() == otherSpot.getDayOfWeek() 
				&& this.getHourOfDay() == otherSpot.getHourOfDay() 
				&& this.getStartTime() == otherSpot.getStartTime() 
				&& this.getEndTime() == otherSpot.getEndTime()
				&& this.getPrice() == otherSpot.getPrice();
		return isEqual;
	}
	
	@Override
	public int hashCode() {
		int multiplierOddNumber = this.getDayOfWeek().getValue() * 2 + 1;
		int initialOddNumber = this.getHourOfDay().getHour() * 2 + 1;
		int hash = new HashCodeBuilder(initialOddNumber, multiplierOddNumber)
				.append(price)
				.append(startTime)
				.append(endTime)
				.hashCode();
		return hash;
	}
	
	@Override
	public String toString() {
		StringBuilder sbldr = new StringBuilder();
		sbldr.append(" day:").append(dayOfWeek)
			.append(" hour:").append(this.getHourOfDay())
			.append(" start:").append(this.getStartTime())
			.append(" end:").append(this.getEndTime())
			.append(" price:").append(this.getPrice());
		return sbldr.toString();
	}
}
