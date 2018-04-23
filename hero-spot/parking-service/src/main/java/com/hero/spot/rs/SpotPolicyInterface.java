package com.hero.spot.rs;

import java.time.LocalTime;

import com.hero.spot.domain.Spot;

/**
 * SpotPolicy evaluates the request's start-time and end-time against found spot.
 * 
 * Decouples business policy from spot and rate.
 *
 */
public interface SpotPolicyInterface {

	String evaluateRequest(LocalTime startTime, LocalTime endTime, Spot found);
}
