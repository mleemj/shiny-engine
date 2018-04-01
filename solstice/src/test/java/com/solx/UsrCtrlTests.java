package com.solx;

import static org.junit.Assert.assertEquals;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;

import com.google.gson.Gson;
import com.solx.domain.Usr;

@RunWith(SpringRunner.class)
@SpringBootTest
@AutoConfigureMockMvc
public class UsrCtrlTests {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void createUser() throws Exception {
    		String name = "solstice";
    		String email = "solstice@email.com";
    		String office = "S-123-456-7890";
    		String home = "S-123-456-7890";

        MvcResult result = this.mockMvc.perform(
        							post("/create")
        								.param("uname", name)
        								.param("uemail", email)
        								.param("uoffice", office)
        								.param("uhome", home))
                .andDo(print()).andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value(name))
                	.andReturn();
        String response = result.getResponse().getContentAsString().trim();
        Gson gson = new Gson();
        Usr savedUser = gson.fromJson(response, Usr.class);
        assertEquals(savedUser.getName(), name);
        assertEquals(savedUser.getPhoneOffice(), office);
        assertEquals(savedUser.getPhoneHome(), home);
        System.out.println("Test createUser");
        System.out.println("------------------------------");
        System.out.println(savedUser);
    }
}