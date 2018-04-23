package com.hero.spot.domain;

import java.time.DayOfWeek;
import java.time.LocalTime;

public class Ohare implements Facility{
	private 	Spot[][] availableSpots = new Spot[7][24];
	
	public Ohare(Spot[][] spots) {
		this.availableSpots = spots;
	}

	public Spot[][] getAvailableSpots() {
		return availableSpots;
	}

	public void setAvailableSpots(Spot[][] availableSpots) {
		this.availableSpots = availableSpots;
	}

	@Override
	public Spot getSpot(DayOfWeek d, LocalTime hr) {
		int day = d.getValue() -1;
		int hour = hr.getHour();
		return this.availableSpots[day][hour];
	}

}
