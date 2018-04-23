package com.hero.spot.repo;

import java.time.DayOfWeek;
import java.time.LocalTime;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.apache.commons.lang3.StringUtils;

import com.hero.spot.domain.Facility;
import com.hero.spot.domain.Ohare;
import com.hero.spot.domain.Spot;

public class RateParser {
	Spot[][] availableSpots = new Spot[7][24];

	public RateParser() {
		for (int day = 0; day < 7; day++) {
			for (int hour = 0; hour < 24; hour++) {
				Spot spot = new Spot();
				DayOfWeek dayOfWeek = DayOfWeek.of(day + 1);
				spot.setDayOfWeek(dayOfWeek);
				LocalTime hourOfDay = LocalTime.of(hour, 0);
				spot.setHourOfDay(hourOfDay);
				availableSpots[day][hour] = spot;
			}
		}
	}

	public Facility parseRate(List<Rate> rates) {
		for (Rate r : rates) {
			String[] dayString = StringUtils.split(r.getDays(), ',');
			String[] timeString = StringUtils.split(r.getTimes(), '-');
			
			String startHr = timeString[0].substring(0, 2);
			String startMin = timeString[0].substring(2);

			String endHr = timeString[1].substring(0, 2);
			String endMin = timeString[1].substring(2);

			Integer price = r.getPrice();
			this.occupySpot(dayString, startHr, startMin, endHr, endMin, price);
		}
		return new Ohare(availableSpots);
	}

	private void occupySpot(String[] days, String startHour, String startMin, String endHour,
			String endMin, Integer price) {
		Set<DayOfWeek> daysOfWeek = getDays(days);
		int startSpotHour = Integer.parseInt(startHour);
		
		LocalTime startTime = LocalTime.of(Integer.parseInt(startHour), Integer.parseInt(startMin));
		LocalTime endTime = LocalTime.of(Integer.parseInt(endHour), Integer.parseInt(endMin));
		
		int endSpotHour = endTime.getHour();
		for(DayOfWeek d: daysOfWeek) {
			int dayIndx = d.getValue() -1;
			for (int hourIndx = startSpotHour; hourIndx <= endSpotHour; hourIndx++) {
				Spot hero = availableSpots[dayIndx][hourIndx];
				hero.setStartTime(startTime);
				hero.setEndTime(endTime);
				hero.setPrice(price);				
			}
		}
	}

	private Set<DayOfWeek> getDays(String[] days) {
		Set<DayOfWeek> dayOfWeek = new HashSet<>();
		for (String d : days) {
			if (d.equalsIgnoreCase("sun")) {
				dayOfWeek.add(DayOfWeek.SUNDAY);
			}
			if (d.equalsIgnoreCase("mon")) {
				dayOfWeek.add(DayOfWeek.MONDAY);
			}
			if (d.equalsIgnoreCase("tues")) {
				dayOfWeek.add(DayOfWeek.TUESDAY);
			}
			if (d.equalsIgnoreCase("wed")) {
				dayOfWeek.add(DayOfWeek.WEDNESDAY);
			}
			if (d.equalsIgnoreCase("thurs")) {
				dayOfWeek.add(DayOfWeek.THURSDAY);
			}
			if (d.equalsIgnoreCase("fri")) {
				dayOfWeek.add(DayOfWeek.FRIDAY);
			}
			if (d.equalsIgnoreCase("sat")) {
				dayOfWeek.add(DayOfWeek.SATURDAY);
			}
		}
		return dayOfWeek;
	}
}
