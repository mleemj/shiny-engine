package com.hero.spot.domain;

import java.time.DayOfWeek;
import java.time.LocalTime;

/**
 * Facility's available spots are represented by
 * a two dimensional array made up of DayOfWeek rows
 * and LocalTime columns.
 * 
 * Monday 0100 = availableSpots[0][1]
 *
 */
public interface Facility {

	/**
	 * Get Spot given the day of the week and the hour.
	 * If the spot is available for booking, it will contain the 
	 * start-time, end-time and price.
	 * 
	 * @param d
	 * @param hr
	 * @return
	 */
	Spot getSpot(DayOfWeek d, LocalTime hr);
	
	Spot[][] getAvailableSpots();
}
