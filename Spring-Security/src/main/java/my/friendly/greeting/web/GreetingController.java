package my.friendly.greeting.web;

import org.springframework.security.web.csrf.CsrfToken;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Optional;
import java.util.concurrent.atomic.AtomicLong;

/**
 *
 * Use Spring MVC RestController annotation
 * Enable COR
 * Use RequestParameter annotation to get value from request
 * Enable Csrf protection (handled in SecurityConfig)
 * Demonstrate how CsrfTokenArgumentResolver provide CSRF token
 * (transparent to RestController)
 * Use Optionals class from Java SDK
 *
 */
@RestController
public class GreetingController {
    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    @CrossOrigin
    @GetMapping("/csrfgreeting")
    public Greeting csrf_greeting(@RequestParam(required = false,
            defaultValue =
                    "World") String name) {
        System.out.println("==== in csrf greeting controller ====");
        return new Greeting(Optional.of(counter.incrementAndGet()), String
                .format(template, name));
    }


    @CrossOrigin
    @GetMapping("/greeting")
    public Greeting greeting(@RequestParam(required = false, defaultValue =
            "World") String name) {
        System.out.println("==== in greeting controller ====");
        return new Greeting(Optional.of(counter.incrementAndGet()), String
                .format(template, name));
    }

    @CrossOrigin({"http://localhost:4200", "http://localhost"})
    @GetMapping({"/", "/home"})
    public Greeting welcome() {
        return new Greeting(Optional.empty(), "This is home");
    }


    @CrossOrigin({"http://localhost:4200", "http://localhost"})
    @GetMapping({"/csrf"})
    public CsrfToken csrfToken(CsrfToken csrfToken) {
        return csrfToken;
    }

}

class Greeting {

    private final long id;
    private final String content;

    public Greeting() {
        this.id = -1;
        this.content = "";
    }

    /**
     * Uses Optional and Long primitive
     */
    public Greeting(Optional<Long> option_id, String content) {
        this.id = option_id.orElse(-1L);
        this.content = content;
    }

    public long getId() {
        return id;
    }

    public String getContent() {
        return content;
    }
}