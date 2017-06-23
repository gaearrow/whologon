# whologon

Collect logon/logoff information

Run better on Domain Controller

**Test on**

Windows Server 2008 X64 R2

Windows 7 X64


## Usage

Run whologon.bat as administrator


## Several Situations

### Logon at keyboard and screen of system

35;Logon;2014-06-24T07:22:56.515;Administrator;WIN-T6I0355NJEA;0x322d3;Interactive;WIN-T6I0355NJEA;127.0.0.1;User32

### Domain user logon domain computer on interaction

1640;Logon;2017-03-27T12:44:41.345;aduser01;OHMYAD;0x8a54d;Network;;192.168.20.151;Kerberos

1520;Logon;2017-03-27T12:38:38.941;Administrator;OHMYAD;0x4d7a3;Network;;192.168.20.151;Kerberos

### Connection to shared folder on the computer from elsewhere on network

6362;Logon;2017-03-28T03:20:53.593;Administrator;OHMYAD;0x47be46;Network;WIN-KMLLOT8IEP7;192.168.20.150;NtLmSsp

15139;Logon;2017-04-13T01:53:29.699;dcadmin;OHMYAD;0xdd428;Network;HELLO-PC;192.168.20.195;NtLmSsp

### Local user logon domain computer on interaction

15122;Logon;2017-04-13T01:49:21.190;ANONYMOUS LOGON;NT AUTHORITY;0xd6e5a;Network;HELLO-PC;192.168.20.195;NtLmSsp


## Column Introduction

### Event No./Task/Date

Base Info.

### Account Name

Logon name of the account

### Account Domain

Domain name of the account (pre-Win2k domain name)

### Logon ID

a semi-unique (unique between reboots) number that identifies the logon session just initiated.  Any events logged subsequently during this logon session will report the same Logon ID through to the logoff event 4647 or 4634.

### Logon Type

2   Interactive (logon at keyboard and screen of system)

3 	Network (i.e. connection to shared folder on this computer from elsewhere on network)

4 	Batch (i.e. scheduled task)

5 	Service (Service startup)

7 	Unlock (i.e. unnattended workstation with password protected screen saver)

8 	NetworkCleartext (Logon with credentials sent in the clear text. Most often indicates a logon to IIS with "basic authentication") See this article for more information.

9 	NewCredentials such as with RunAs or mapping a network drive with alternate credentials.  This logon type does not seem to show up in any events.  If you want to track users attempting to logon with alternate credentials see 4648.

10 	RemoteInteractive (Terminal Services, Remote Desktop or Remote Assistance)

11 	CachedInteractive (logon with cached domain credentials such as when logging on to a laptop when away from the network)

### Workstation Name

the computer name of the computer where the user is physically present in most cases unless this logon was intitiated by a server application acting on behalf of the user.  Workstation may also not be filled in for some Kerberos logons since the Kerberos protocol doesn't really care about the computer account in the case of user logons and therefore lacks any field for carrying workstation name in the ticket request message.

### Logon Address

(Source Network Address) the IP address of the computer where the user is physically present in most cases unless this logon was intitiated by a server application acting on behalf of the user.  If this logon is initiated locally the IP address will sometimes be 127.0.0.1 instead of the local computer's actual IP address.  This field is also blank sometimes because Microsoft says "Not every code path in Windows Server 2003 is instrumented for IP address, so it's not always filled out."

### Logon Process

A logon process is a trusted part of the operating system and handles the overall logon function for different logon methods including incoming RAS connections, RunAs, interactive logons initiated by CtrlAltDel, and network logons (as in drive mappings).

Because logon processes are such trusted functions, a rogue logon process would be a devastating security breach--but an improbable one, given the effort and skill required.

Standard logon processes for Windows Server 2008:

    Winlogon
	
    Schannell
	
    KSecDD
	
    Secondary Logon Service (runas)
	
    IKE
	
    HTTP.SYS
	
    SspTest
	
    dsRole
	
    DS Replication CredProvConsent (user account control)
	
### Refer

https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4624

https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4611