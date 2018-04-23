package com.hero.spot.rs;

import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.logging.Logger;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;

import com.hero.spot.domain.Facility;
import com.hero.spot.domain.Spot;
import com.hero.spot.repo.RateRepo;

@Path("/spotresource")
public class SpotResource {

	private Logger logger = Logger.getLogger(SpotResource.class.getName());
	private SpotPolicyInterface policy = new SpotPolicy();


	@GET
	@Produces(MediaType.TEXT_PLAIN)
	public String ratePlainText(@QueryParam("start") String fromDataTime, @QueryParam("stop") String toDataTime) {
		String rate = this.getRate(fromDataTime, toDataTime);
		return rate;
	}

	@GET
	@Produces(MediaType.APPLICATION_XML)
	public SpotResponse rateXML(@QueryParam("start") String fromDataTime, @QueryParam("stop") String toDataTime) {
		String rate = this.getRate(fromDataTime, toDataTime);
		return new SpotResponse(rate);
	}

	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public SpotResponse rateJson(@QueryParam("start") String fromDataTime, @QueryParam("stop") String toDataTime) {
		String rate = this.getRate(fromDataTime, toDataTime);
		return new SpotResponse(rate);
	}

	// This method is called if HTML is request
	@GET
	@Produces(MediaType.TEXT_HTML)
	public String rateHtml(@QueryParam("start") String fromDataTime, @QueryParam("stop") String toDataTime) {
		String rate = this.getRate(fromDataTime, toDataTime);
		return "<html> " + "<title>" + "SpotHero" + "</title>" + "<body><h1>" + rate + "</body></h1>" + "</html> ";
	}

	private String getRate(String fromDataTime, String toDataTime) {
		RateRepo repo = new RateRepo();
		Facility facility = repo.getFacility();
		Spot[][] availableSpots = facility.getAvailableSpots();

		LocalDateTime startDateTime = getDateTime(fromDataTime);
		LocalTime startTime = startDateTime.toLocalTime();
		LocalTime endTime = getDateTime(toDataTime).toLocalTime();
		//DayOfWeek begins from 1 to 7
		int dayIndx = startDateTime.getDayOfWeek().getValue() - 1;
		int hourIndx = startTime.getHour();
		Spot foundSpot = availableSpots[dayIndx][hourIndx];
		
		String response = policy.evaluateRequest(startTime, endTime, foundSpot);
		return response;
	}
	public static LocalDateTime getDateTime(String datetime) {
		return LocalDateTime.parse(datetime, DateTimeFormatter.ISO_DATE_TIME);
	}
}
