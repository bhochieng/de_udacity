import smtplib

# creates SMTP session
s = smtplib.SMTP('ssmtp.mailgun.org', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("opostmaster@sandboxeb2e2bc5200f4c6bb8292bb20c3dbcd2.mailgun.org", "14d30aa48459242b1224e8241ac4924f-31eedc68-eb845b05")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("oneeyedexplorer@gmail.com", "developer.humphrey@gmail.com", message)

# terminating the session
s.quit()


select * from sms_tag.tbl_ekyc_greylist_ group by run_date


create or replace procedure NOTIFY_PLEASECALLME ( P_MSISDN IN NUMBER, P_MESSAGE_TYPE IN VARCHAR2) RETURN VARCHAR2 AS 

p_sender varchar2(160);
v_MSISDN number :=0;
v_NDC number :=0;
v_OFFER_ID number:=1;
p_cnt number :=0;

BEGIN

v_MSISDN:=substr(P_MSISDN,-9);
v_ndc := substr(P_MSISDN,4,3);

    SELECT aa.sender into p_sender FROM tbl_sc_msgs aa where aa.offer_id=v_OFFER_ID;
    return p_sender;
  
END SC_RCHRG_MSG_SENDER;
/
CREATE OR REPLACE PROCEDURE NOTIFY_PLEASECALLME (p_to IN VARCHAR2,
                                       p_from      IN VARCHAR2,
                                       p_message   IN VARCHAR2,
                                       p_smtp_host IN VARCHAR2,
                                       p_smtp_port IN NUMBER DEFAULT 25)
AS
  l_mail_conn   UTL_SMTP.connection;
BEGIN
  l_mail_conn := UTL_SMTP.open_connection(p_smtp_host, p_smtp_port);
  UTL_SMTP.helo(l_mail_conn, p_smtp_host);
  UTL_SMTP.mail(l_mail_conn, p_from);
  UTL_SMTP.rcpt(l_mail_conn, p_to);
  UTL_SMTP.data(l_mail_conn, p_message || UTL_TCP.crlf || UTL_TCP.crlf);
  UTL_SMTP.quit(l_mail_conn);
END;
/
CREATE OR REPLACE PROCEDURE notify_user 
AS 
v_total_count NUMBER;
v_date NUMBER;
v_sys_date NUMBER DEFAULT TO_NUMBER(TO_CHAR(SYSDATE,'YYYYMMDD'));

BEGIN 
	SELECT COUNT(*),RUN_DATE 
	INTO v_total_count,v_date
	FROM CVM_DM_LND.TBL_EKYC_GREYLIST_H gc 
	GROUP BY RUN_DATE ;
	--dbms_output.put_line('HI' || v_total_count || v_date||v_sys_date);
	-- condition to check the records.
    IF v_sys_date != v_date THEN 
       dbms_output.put_line('Should send a notification');
       --call the send notification function.
    ELSE 
       dbms_output.put_line('No sending notification');
    END IF;
END;
/
BEGIN
	notify_user;
END;
