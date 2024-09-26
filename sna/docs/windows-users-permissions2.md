Here are some additional practical tasks related to managing user accounts and file permissions on Windows:

### Task 1: Changing Password for a User Account
**Objective:** Change the password for an existing user account using the Admin account.

1. Log in with the Admin account.
2. Open **Control Panel** > **User Accounts** > **Manage another account**.
3. Select the user whose password you want to change.
4. Click **Change the password**, enter the new password, and confirm.
5. Log out and verify that the password change is successful.

### Task 3: Apply Read-Only Permissions to a Folder for a User
**Objective:** Set up a folder that a standard user can access but only with read-only permissions.

1. Log in with the Admin account.
2. Create a folder in **D: drive** (e.g., **ReadOnlyFolder**).
3. Right-click the folder and select **Properties** > **Security**.
4. Add the standard user account and set **Read & Execute** and **Read** permissions while denying **Write**.
5. Log in with the standard user account and verify that the user can only read the files but cannot modify them.



### Task 6: Create a Shared Folder with Specific Permissions for Multiple Users
**Objective:** Create a shared folder on the network with different permission levels for different users.

1. Log in with the Admin account.
2. Create a folder on the **D: drive** (e.g., **SharedFolder**).
3. Right-click the folder and select **Properties** > **Sharing** > **Advanced Sharing**.
4. Enable sharing and click **Permissions**.
5. Add multiple users and set different permissions (e.g., full control for one user, read-only for another).
6. Test by logging in as different users to verify permission levels.

### Task : Auditing File Access Attempts
**Objective:** Set up auditing to track file access attempts for specific users.

1. Log in with the Admin account.
2. Right-click the folder (e.g., **SensitiveData**) and go to **Properties** > **Security** > **Advanced**.
3. Go to the **Auditing** tab and click **Add**.
4. Select the users whose access attempts you want to audit and choose which actions (e.g., read, write) should trigger an audit log.
5. Review the audit logs in **Event Viewer** to monitor access attempts.



## Create new user using computer management

## Access Shared folders in Computer management

## Install Office 365
[Download and install or reinstall Microsoft 365 (for students)](https://gudgk.github.io/gu-userguides/microsoft365/install-microsoft365.html)
