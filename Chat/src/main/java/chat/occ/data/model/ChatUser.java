package chat.occ.data.model;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;

public class ChatUser extends User {
	private Long usrId;
	private String usrName;
	private String usrEmail;
	private String usrPassword;
	private String usrRole;
	private boolean usrEnabled;

	public ChatUser(Long usrId, String usrName, String usrEmail, String usrPassword, String usrRole,
			boolean usrEnabled) {
		super(usrName, usrPassword, GetAuthorities(usrRole));
		this.usrId = usrId;
		this.usrName = usrName;
		this.usrEmail = usrEmail;
		this.usrPassword = usrPassword;
		this.usrRole = usrRole;
		this.usrEnabled = usrEnabled;
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		return sb.append(getUsrId())
				.append(' ')
				.append(getUsrName())
				.append(' ')
				.append(getUsrEmail())
				.append(' ')
				.append(getUsrPassword())
				.append(' ')
				.append(getUsrRole())
				.append(' ')
				.append(getUsrEnabled())
				.append(' ')
				.toString();
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

	public String getUsrRole() {
		return usrRole;
	}

	public void setUsrRole(String usrRole) {
		this.usrRole = usrRole;
	}

	public boolean getUsrEnabled() {
		return usrEnabled;
	}

	public void setUsrEnabled(boolean usrEnabled) {
		this.usrEnabled = usrEnabled;
	}

	public static Collection<GrantedAuthority> GetAuthorities(String usrRole) {
		List<GrantedAuthority> authorities = new ArrayList<GrantedAuthority>();
		SimpleGrantedAuthority sga = new SimpleGrantedAuthority(usrRole);
		authorities.add(sga);
		return authorities;
	}
}
