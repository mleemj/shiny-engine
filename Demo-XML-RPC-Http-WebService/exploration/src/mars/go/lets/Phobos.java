package mars.go.lets;

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

import fried.peanut.butter.Book;
import fried.peanut.butter.ObjectFactory;

@WebService(name = "Phobos", targetNamespace = "http://lets.go.mars/")
@SOAPBinding(style=Style.RPC)
public class Phobos {

	// @WebMethod operationName map to WSDL, action map to SOAPAction
	@WebMethod(operationName="operationGetBook", action="actionGetBook")
	public Book getBook(@WebParam(name="titleparam")String booktitle
			, @WebParam(name="authorparam")String bookauthor
			, @WebParam(name="priceparam") int bookprice){
		
		//Use the ObjectFactory to create new instances of the objects
		ObjectFactory factory = new ObjectFactory();
		Book spacebook = factory.createBook();
		spacebook.setTitle(booktitle.toUpperCase());
		spacebook.setAuthor(bookauthor.toUpperCase());
		spacebook.setPrice(bookprice * 2);
		return spacebook;
	}
}
