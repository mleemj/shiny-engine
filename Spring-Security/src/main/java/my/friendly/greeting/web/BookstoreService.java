package my.friendly.greeting.web;

import my.friendly.greeting.fromxsdtojava.Bookstore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public class BookstoreService {
    @Autowired
    @Qualifier("bookstore")
    private Bookstore bookstore;


    @WebMethod
    public Bookstore getBookstore(){
        return bookstore;
    }
}
