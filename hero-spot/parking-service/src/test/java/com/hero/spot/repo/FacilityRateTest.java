package com.hero.spot.repo;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import java.time.DayOfWeek;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

import org.junit.Before;
import org.junit.Test;

import com.hero.spot.domain.Facility;
import com.hero.spot.domain.Spot;

/**
 * Main test to check the validity of the algorithm
 * 
 * Rates are from the assignment
 * 
 */
public class FacilityRateTest {
	private List<Rate> rates;
	private Logger logger = Logger.getLogger(FacilityRateTest.class.getName());

	@Before
	public void setUp() {
		rates = new ArrayList();

		Rate r1 = new Rate();
		r1.setDays("mon,tues,thurs");
		r1.setTimes("0900-2100");
		r1.setPrice(1500);

		rates.add(r1);

		Rate r2 = new Rate();
		r2.setDays("fri,sat,sun");
		r2.setTimes("0900-2100");
		r2.setPrice(2000);

		rates.add(r2);

		Rate r3 = new Rate();
		r3.setDays("wed");
		r3.setTimes("0600-1800");
		r3.setPrice(1750);

		rates.add(r3);

		Rate r4 = new Rate();
		r4.setDays("mon,wed,sat");
		r4.setTimes("0100-0500");
		r4.setPrice(1000);

		rates.add(r4);

		Rate r5 = new Rate();
		r5.setDays("sun,tues");
		r5.setTimes("0100-0700");
		r5.setPrice(925);

		rates.add(r5);
	}

	@Test
	public void testSundayAvailableHours() {
		RateParser rateparser = new RateParser();
		Facility facility = rateparser.parseRate(rates);
		assertNotNull(facility);

		for (int h = 1; h <= 7; h++) {
			LocalTime hour = LocalTime.of(h, 0);
			Spot foundSpot = facility.getSpot(DayOfWeek.SUNDAY, hour);
			if (h == 7) {
				assertFalse(hour.isBefore(foundSpot.getEndTime()));
			}
			testAvailableHours(foundSpot, hour, DayOfWeek.SUNDAY);
		}

		for (int h = 9; h <= 21; h++) {
			LocalTime hour = LocalTime.of(h, 0);
			Spot foundSpot = facility.getSpot(DayOfWeek.SUNDAY, hour);
			if (h == 21) {
				assertFalse(hour.isBefore(foundSpot.getEndTime()));
			}
			testAvailableHours(foundSpot, hour, DayOfWeek.SUNDAY);
		}
	}

	private void testAvailableHours(Spot foundSpot, LocalTime hour, DayOfWeek day) {
		assertNotNull(foundSpot.getPrice());
		assertNotNull(foundSpot.getStartTime());
		assertNotNull(foundSpot.getEndTime());
		assertEquals(hour, foundSpot.getHourOfDay());
		assertEquals(day, foundSpot.getDayOfWeek());
	}

	@Test
	public void testSundayUnavailableHours() {
		RateParser rateparser = new RateParser();
		Facility facility = rateparser.parseRate(rates);
		assertNotNull(facility);
		LocalTime unavailableHour = LocalTime.of(0, 0);
		Spot unoccupiedSpot = facility.getSpot(DayOfWeek.SUNDAY, unavailableHour);
		testUnavailableHour(unoccupiedSpot, unavailableHour, DayOfWeek.SUNDAY);

		unavailableHour = LocalTime.of(8, 0);
		unoccupiedSpot = facility.getSpot(DayOfWeek.SUNDAY, unavailableHour);
		testUnavailableHour(unoccupiedSpot, unavailableHour, DayOfWeek.SUNDAY);

		unavailableHour = LocalTime.of(22, 0);
		unoccupiedSpot = facility.getSpot(DayOfWeek.SUNDAY, unavailableHour);
		testUnavailableHour(unoccupiedSpot, unavailableHour, DayOfWeek.SUNDAY);

		unavailableHour = LocalTime.of(23, 0);
		unoccupiedSpot = facility.getSpot(DayOfWeek.SUNDAY, unavailableHour);
		testUnavailableHour(unoccupiedSpot, unavailableHour, DayOfWeek.SUNDAY);
	}

	private void testUnavailableHour(Spot unoccupiedSpot, LocalTime hour, DayOfWeek day) {
		assertTrue(unoccupiedSpot.getPrice() == null);
		assertTrue(unoccupiedSpot.getStartTime() == null);
		assertTrue(unoccupiedSpot.getEndTime() == null);
		assertEquals(unoccupiedSpot.getDayOfWeek(), day);
		assertEquals(unoccupiedSpot.getHourOfDay(), hour);
	}

	@Test
	public void testMidNiteHour() {
		RateParser rateparser = new RateParser();
		Facility facility = rateparser.parseRate(rates);
		assertNotNull(facility);
		Spot[][] availableSpots = facility.getAvailableSpots();
		assertNotNull(availableSpots);
		
		LocalTime tZero = LocalTime.of(0, 0);
		Spot mondayMidNite = facility.getSpot(DayOfWeek.MONDAY, tZero);
		assertNull(mondayMidNite.getPrice());
		assertNull(mondayMidNite.getStartTime());
		assertNull(mondayMidNite.getEndTime());
		assertEquals(DayOfWeek.MONDAY, mondayMidNite.getDayOfWeek());
		assertEquals(tZero, mondayMidNite.getHourOfDay());
	}

	@Test
	public void testEndTime() {
		RateParser rateparser = new RateParser();
		Facility facility = rateparser.parseRate(rates);
		assertNotNull(facility);
		Spot[][] availableSpots = facility.getAvailableSpots();
		assertNotNull(availableSpots);

		LocalTime t21 = LocalTime.of(21, 0);
		Spot monday9PM = facility.getSpot(DayOfWeek.MONDAY, t21);
		assertNotNull(monday9PM.getPrice());
		assertNotNull(monday9PM.getStartTime());
		assertNotNull(monday9PM.getEndTime());
		assertEquals(DayOfWeek.MONDAY, monday9PM.getDayOfWeek());
		assertEquals(t21, monday9PM.getHourOfDay());
		assertFalse(t21.isBefore(monday9PM.getEndTime()));
	}

	@Test
	public void testAvailableTime() {
		RateParser rateparser = new RateParser();
		Facility facility = rateparser.parseRate(rates);
		assertNotNull(facility);
		Spot[][] availableSpots = facility.getAvailableSpots();
		assertNotNull(availableSpots);

		LocalTime t20 = LocalTime.of(20, 0);
		Spot monday8PM = facility.getSpot(DayOfWeek.MONDAY, t20);
		assertNotNull(monday8PM.getPrice());
		assertNotNull(monday8PM.getStartTime());
		assertNotNull(monday8PM.getEndTime());
		assertEquals(DayOfWeek.MONDAY, monday8PM.getDayOfWeek());
		assertEquals(t20, monday8PM.getHourOfDay());
		assertTrue(t20.isBefore(monday8PM.getEndTime()));
	}

	@Test
	public void testStartTime() {
		RateParser rateparser = new RateParser();
		Facility facility = rateparser.parseRate(rates);
		assertNotNull(facility);
		Spot[][] availableSpots = facility.getAvailableSpots();
		assertNotNull(availableSpots);

		LocalTime t9 = LocalTime.of(9, 0);
		Spot monday9AM = facility.getSpot(DayOfWeek.MONDAY, t9);
		assertNotNull(monday9AM.getPrice());
		assertNotNull(monday9AM.getStartTime());
		assertNotNull(monday9AM.getEndTime());
		assertEquals(DayOfWeek.MONDAY, monday9AM.getDayOfWeek());
		assertEquals(t9, monday9AM.getHourOfDay());
		assertTrue(t9.isBefore(monday9AM.getEndTime()));
	}
}
