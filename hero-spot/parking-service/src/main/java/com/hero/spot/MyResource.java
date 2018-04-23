package com.hero.spot;

import java.util.logging.Logger;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.codahale.metrics.Timer;
import com.hero.spot.domain.Facility;
import com.hero.spot.domain.Spot;
import com.hero.spot.repo.RateRepo;

/**
 * Provide metrics on mean time to build facility
 * 
 */
@Path("/myresource")
public class MyResource {
	private Logger logger = Logger.getLogger(MyResource.class.getName());

	// This method is called if TEXT_PLAIN is request
	@GET
	@Produces(MediaType.TEXT_PLAIN)
	public String resourceMeanTime() {
		Timer timer = new Timer();
		Timer.Context c = timer.time();
		RateRepo repo = new RateRepo();
		Facility facility = repo.getFacility();
		Spot[][] availableSpots = facility.getAvailableSpots();
		for (int i = 0; i < 7; i++) {
			for (int j = 0; j < 24; j++) {
				Spot hero = availableSpots[i][j];
				if (hero.getEndTime() != null) {
					logger.info(hero.toString());
				}
			}
		}
		c.stop();
		return "Time taken to build Facility " + timer.getMeanRate();
	}

	// This method is called if XML is request
	@GET
	@Produces(MediaType.TEXT_XML)
	public String resourceMeanTimeXML() {
		Timer timer = new Timer();
		Timer.Context c = timer.time();
		RateRepo repo = new RateRepo();
		Facility facility = repo.getFacility();
		Spot[][] availableSpots = facility.getAvailableSpots();
		for (int i = 0; i < 7; i++) {
			for (int j = 0; j < 24; j++) {
				Spot hero = availableSpots[i][j];
				if (hero.getEndTime() != null) {
					logger.info(hero.toString());
				}
			}
		}
		c.stop();
		return "<?xml version=\"1.0\"?>" + "<time> " + timer.getMeanRate() + "</time>";
	}

	// This method is called if HTML is request
	@GET
	@Produces(MediaType.TEXT_HTML)
	public String resourceMeanTimeHTML() {
		Timer timer = new Timer();
		Timer.Context c = timer.time();
		RateRepo repo = new RateRepo();
		Facility facility = repo.getFacility();
		Spot[][] availableSpots = facility.getAvailableSpots();
		for (int i = 0; i < 7; i++) {
			for (int j = 0; j < 24; j++) {
				Spot hero = availableSpots[i][j];
				if (hero.getEndTime() != null) {
					logger.info(hero.toString());
				}
			}
		}
		c.stop();
		return "<html> " + "<title>" + "HeroSpot" + "</title>" + "<body><h1>" + timer.getMeanRate() + "</body></h1>"
				+ "</html> ";
	}
}
