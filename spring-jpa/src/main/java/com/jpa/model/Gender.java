package com.jpa.model;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;


/**
 * The persistent class for the gender_submission database table.
 * 
 */
//@Table(name="gender_submission")
//table name does not need to include database.tablename
@Entity
public class Gender implements Serializable {
	private static final long serialVersionUID = 1L;

	@Id
    @GeneratedValue(strategy=GenerationType.AUTO)
	private Integer passengerId;

	private Integer survived;
	
	public Gender() {}

	public Gender(Integer safe) {
		this.survived = safe;
	}

	public Integer getPassengerId() {
		return this.passengerId;
	}

	public void setPassengerId(Integer passengerId) {
		this.passengerId = passengerId;
	}

	public Integer getSurvived() {
		return this.survived;
	}

	public void setSurvived(Integer survived) {
		this.survived = survived;
	}

}