package com.hero.spot.repo;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.logging.Logger;

import org.apache.commons.io.IOUtils;

import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;

public class RateDatasource {
	private Logger logger = Logger.getLogger(RateDatasource.class.getName());
	private RateInterface ohareRate;
	private static RateDatasource datasource;
	private RateDatasource() {}
	
	public static RateDatasource getInstance() {
		if (datasource == null) {
			datasource = new RateDatasource();
		}
		return datasource;
	}
	
	public RateInterface getDatasource() {
		if (ohareRate != null) return ohareRate;
		InputStream inputStream = 
				RateDatasource.class.getClassLoader().getResourceAsStream("rate.data.source");
		try {
			List<String> dataFile = IOUtils.readLines(inputStream, StandardCharsets.UTF_8);
			String datasource = dataFile.get(0);
			InputStream entity = RateDatasource.class
							.getClassLoader()
							.getResourceAsStream(datasource);
			JsonReader reader = new JsonReader(new InputStreamReader(entity));
			Gson gson = new Gson();
			ohareRate = gson.fromJson(reader, OhareRate.class);
		} catch (IOException e) {
			logger.info(e.getMessage());
		}
		return ohareRate;
	}

}
