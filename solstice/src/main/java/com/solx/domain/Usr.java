package com.solx.domain;

import java.time.LocalDateTime;

import org.apache.commons.lang3.StringUtils;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Document
public class Usr {
	@Id
	public String id;

	private String name;
	private String company;
	private String pathToProfileImage;
	private LocalDateTime bdate;

	private Usr() {
	}

	public static Usr makeUsr(String usrName, String usrEmail, String oPhone, String hPhone) {
		if (usrEmail == null || usrEmail == null || oPhone == null || hPhone == null) {
			throw new IllegalArgumentException();
		}
		Usr user = new Usr();
		user.name = usrName;
		user.email = usrEmail;
		user.phoneOffice = oPhone;
		user.phoneHome = hPhone;
		return user;
	}

	@Indexed(unique = true)
	private String email;

	@Indexed(unique = true)
	private String phoneOffice;

	@Indexed(unique = true)
	private String phoneHome;

	@Indexed
	private String state;

	@Indexed
	private String city;

	@Override
	public boolean equals(Object other) {
		if (!(other instanceof Usr))
			return false;
		Usr oUser = (Usr) other;
		if (StringUtils.compare(oUser.email, this.email) == 0
				|| StringUtils.compare(oUser.phoneHome, this.phoneHome) == 0
				|| StringUtils.compare(oUser.phoneOffice, this.phoneOffice) == 0) {
			return true;
		}
		return false;
	}

	@Override
	public int hashCode() {
		HashCodeBuilder bldr = new HashCodeBuilder();
		bldr.append(this.name.toCharArray());
		return bldr.hashCode();
	}

	@Override
	public String toString() {
		StringBuilder sbldr = new StringBuilder();
		sbldr.append(this.name).append("\nO:").append(this.phoneOffice).append("\nH:").append(this.phoneHome)
				.append("\nCity:").append(this.city).append("\nState:").append(this.state);
		return sbldr.toString();
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getCompany() {
		return company;
	}

	public void setCompany(String company) {
		this.company = company;
	}

	public String getPathToProfileImage() {
		return pathToProfileImage;
	}

	public void setPathToProfileImage(String pathToProfileImage) {
		this.pathToProfileImage = pathToProfileImage;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public LocalDateTime getBdate() {
		return bdate;
	}

	public void setBdate(LocalDateTime bdate) {
		this.bdate = bdate;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getPhoneOffice() {
		return phoneOffice;
	}

	public void setPhoneOffice(String phoneOffice) {
		this.phoneOffice = phoneOffice;
	}

	public String getPhoneHome() {
		return phoneHome;
	}

	public void setPhoneHome(String phoneHome) {
		this.phoneHome = phoneHome;
	}
}
