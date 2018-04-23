package com.hero.spot.rs;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class SpotResponse {
	private String rate;
	
	public SpotResponse() {}
	
	public SpotResponse(String r) {
		this.rate = r;
	}

	public String getRate() {
		return rate;
	}

	public void setRate(String rate) {
		this.rate = rate;
	}
}
