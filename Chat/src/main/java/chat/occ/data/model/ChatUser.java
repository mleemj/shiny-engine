package chat.occ.data.model;

import java.security.Key;
import java.util.Collection;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.User;

public class ChatUser extends User {
	private Long usrId;
	private String usrName;
	private String usrEmail;
	private String usrPassword;
	private boolean usrEnabled;
	private Collection<GrantedAuthority> usrAuthorities;
	// immutable key
	final private Key chatUsrJwtKey;
	
	public ChatUser(Long usrId, String usrName, String usrEmail, String usrPassword,
			Collection<GrantedAuthority> authorites, boolean usrEnabled) {
		super(usrName, usrPassword, authorites);
		this.usrId = usrId;
		this.usrName = usrName;
		this.usrEmail = usrEmail;
		this.usrPassword = usrPassword;
		this.usrEnabled = usrEnabled;
		this.usrAuthorities = authorites;
		this.chatUsrJwtKey = ChatJwtHelper.generateKey();
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		return sb.append(getUsrId()).append(' ').append(getUsrName()).append(' ').append(getUsrEmail()).append(' ')
				.append(getUsrPassword()).append(' ').append(getAuthorities()).append(' ').append(getUsrEnabled())
				.append(' ').toString();
	}

	@Override
	public boolean equals(Object o) {
		if (this == o)
			return true;

		if (o == null || getClass() != o.getClass())
			return false;

		ChatUser cu = (ChatUser) o;

		return new EqualsBuilder().append(this.getUsrId(), cu.getUsrId()).isEquals();
	}

	@Override
	public int hashCode() {
		return new HashCodeBuilder(17, 37).append(this.getUsrId()).toHashCode();
	}

	public Long getUsrId() {
		return usrId;
	}

	public void setUsrId(Long usrId) {
		this.usrId = usrId;
	}

	public String getUsrName() {
		return usrName;
	}

	public void setUsrName(String usrName) {
		this.usrName = usrName;
	}

	public String getUsrEmail() {
		return usrEmail;
	}

	public void setUsrEmail(String usrEmail) {
		this.usrEmail = usrEmail;
	}

	public String getUsrPassword() {
		return usrPassword;
	}

	public void setUsrPassword(String usrPassword) {
		this.usrPassword = usrPassword;
	}

	public boolean getUsrEnabled() {
		return usrEnabled;
	}

	public void setUsrEnabled(boolean usrEnabled) {
		this.usrEnabled = usrEnabled;
	}

	public Collection<GrantedAuthority> getAuthorities() {
		return this.usrAuthorities;
	}

	public Collection<GrantedAuthority> getUsrAuthorities() {
		return usrAuthorities;
	}

	public void setUsrAuthorities(Collection<GrantedAuthority> usrAuthorities) {
		this.usrAuthorities = usrAuthorities;
	}

	public Key getChatUsrJwtKey() {
		return chatUsrJwtKey;
	}
}
