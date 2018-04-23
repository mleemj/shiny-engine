package com.hero.spot.rs;

import java.time.LocalTime;

import com.hero.spot.domain.Spot;

public class SpotPolicy implements SpotPolicyInterface {

	@Override
	public String evaluateRequest(LocalTime requestStartTime, LocalTime requestEndTime, Spot found) {
		String response = "unavailable";
		LocalTime spotStartTime = found.getStartTime();		
		LocalTime spotEndTime = found.getEndTime();
		if ((spotStartTime == null) || (requestStartTime.isBefore(spotStartTime))) {
			return response;
		}
		if ((spotEndTime != null) && (spotEndTime.isAfter(requestEndTime))) {
			response = found.getPrice().toString();
		}
		return response;
	}

}
