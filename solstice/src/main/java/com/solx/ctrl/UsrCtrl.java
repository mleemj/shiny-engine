package com.solx.ctrl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.solx.domain.Usr;
import com.solx.repo.UsrRepo;

@RestController
public class UsrCtrl {
	
	@Autowired
	UsrRepo repository;
	
	@RequestMapping(name="/create", method=RequestMethod.POST)
	public @ResponseBody Usr createUsr(@RequestParam(value="uname") String usrName,
			@RequestParam(value="uemail") String usrEmail, 
			@RequestParam(value="uoffice") String oPhone,
			@RequestParam(value="uhome") String hPhone){
		Usr user = Usr.makeUsr(usrName, usrEmail, oPhone, hPhone);
		repository.save(user);
		return user;
	}

}

//public static Usr makeUsr(String usrName, String usrEmail, String oPhone, String hPhone) 