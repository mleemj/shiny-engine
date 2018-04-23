package com.hero.spot.rs;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.time.DayOfWeek;
import java.time.LocalTime;

import org.junit.Test;

import com.hero.spot.domain.Spot;

public class SpotPolicyTest {

	@Test
	public void testAvailableSpot() {
		SpotPolicyInterface policy = new SpotPolicy();
		Spot found = new Spot();
		LocalTime spotStartTime = LocalTime.of(1, 0);
		LocalTime spotEndTime = LocalTime.of(3, 0);
		
		found.setDayOfWeek(DayOfWeek.MONDAY);
		found.setHourOfDay(spotStartTime);
		found.setStartTime(spotStartTime);
		found.setEndTime(spotEndTime);
		found.setPrice(Integer.valueOf(100));
		
		LocalTime requestStartTime = LocalTime.of(1, 0);
		LocalTime requestEndTime = LocalTime.of(2, 59);
		
		String response = policy.evaluateRequest(requestStartTime, requestEndTime, found);
		assertEquals(100, Integer.parseInt(response));
	}
	
	@Test
	public void testExcludeEndTime() {
		SpotPolicyInterface policy = new SpotPolicy();
		Spot found = new Spot();
		LocalTime spotStartTime = LocalTime.of(1, 0);
		LocalTime spotEndTime = LocalTime.of(3, 0);
		
		found.setDayOfWeek(DayOfWeek.MONDAY);
		found.setHourOfDay(spotStartTime);
		found.setStartTime(spotStartTime);
		found.setEndTime(spotEndTime);
		found.setPrice(Integer.valueOf(100));
		
		LocalTime requestStartTime = LocalTime.of(1, 0);
		LocalTime requestEndTime = LocalTime.of(3, 0);
		
		String response = policy.evaluateRequest(requestStartTime, requestEndTime, found);
		assertTrue("unavailable".equalsIgnoreCase(response));
	}

}
