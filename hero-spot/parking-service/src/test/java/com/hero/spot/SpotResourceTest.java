package com.hero.spot;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import java.util.logging.Logger;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;

import org.glassfish.grizzly.http.server.HttpServer;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.hero.spot.rs.SpotResponse;

public class SpotResourceTest {

	private HttpServer server;
	private WebTarget target;
	private Logger logger = Logger.getLogger(SpotResourceTest.class.toString());

	@Before
	public void setUp() throws Exception {
		server = Main.startServer();
		Client c = ClientBuilder.newClient();
		target = c.target(Main.BASE_URI);
	}

	@After
	public void tearDown() throws Exception {
		server.stop();
	}

	@Test
	public void testSpotResource() {
		String responseMsg = target.path("spotresource").queryParam("start", "2015-07-04T07:00:00Z")
				.queryParam("stop", "2015-07-04T12:00:00Z").request().get(String.class);
		logger.info("response " + responseMsg);
		assertNotNull(responseMsg);
	}

	@Test
	public void testSpotResourceJson() {
		SpotResponse responseMsg = target.path("spotresource").queryParam("start", "2015-07-04T07:00:00Z")
				.queryParam("stop", "2015-07-04T12:00:00Z").request().accept(MediaType.APPLICATION_JSON)
				.get(SpotResponse.class);
		logger.info("JSON response " + responseMsg.getRate());
		assertNotNull(responseMsg);
		assertEquals(2000, Integer.parseInt(responseMsg.getRate()));
	}

	@Test
	public void testSpotResourceXML() {
		SpotResponse responseMsg = target.path("spotresource").queryParam("start", "2015-07-04T07:00:00Z")
				.queryParam("stop", "2015-07-04T12:00:00Z").request().accept(MediaType.APPLICATION_XML)
				.get(SpotResponse.class);
		logger.info("XML response " + responseMsg.getRate());
		assertNotNull(responseMsg);
		assertEquals(2000, Integer.parseInt(responseMsg.getRate()));
	}
}
