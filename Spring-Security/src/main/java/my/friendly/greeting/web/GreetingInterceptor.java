package my.friendly.greeting.web;

import org.springframework.stereotype.Component;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Enumeration;


/**
 * Intercept request before RestController
 */
@Component
public class GreetingInterceptor extends HandlerInterceptorAdapter {
    @Override
    public boolean preHandle(HttpServletRequest request,
                             HttpServletResponse response, Object handler)
            throws Exception {
        System.out.println("==== in greeting interceptor ====");
        Enumeration<String> headerNames = request.getHeaderNames();
        while (headerNames.hasMoreElements()) {
            String header_name = headerNames.nextElement();
            System.out.println("Header-name: " + header_name);
            System.out.println(request.getHeader(header_name));
        }

        Cookie[] cookie = request.getCookies();
        if (null != cookie && cookie.length != 0) {
            for (Cookie c : cookie) {
                String cookie_name = c.getName();
                String cookie_vaue = c.getValue();
                System.out.println("Coookie " + cookie_name + " " +
                        cookie_vaue);

            }
        } else {
            System.out.println("No cookie found");
        }
        return super.preHandle(request, response, handler);
    }
}
