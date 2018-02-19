package com.conf;

import org.springframework.security.web.csrf.CookieCsrfTokenRepository;
import org.springframework.security.web.csrf.CsrfTokenRepository;
import org.springframework.security.web.util.matcher.RequestMatcher;

/**
 * Customize cookiename and cookieheader
 * SecurityConfig expect token in client request's params={cookieheader=token}
 */
public abstract class AbstractTokenRepository {
    public abstract String getHeaderName();

    public abstract String getCookieName();

    public abstract RequestMatcher getRequireCsrfRequestMatcher();

    public CsrfTokenRepository getTokenRepository() {
        CookieCsrfTokenRepository repository = new
                CookieCsrfTokenRepository();
        repository.setHeaderName(getHeaderName());
        repository.setCookieName(getCookieName());
        repository.setCookieHttpOnly(false);
        return repository;
    }
}
