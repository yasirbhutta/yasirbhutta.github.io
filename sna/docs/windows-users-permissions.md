# Windows:Managing User Accounts and File Permissions on Windows

- [Download PDF](https://yasirbhutta.github.io/sna/docs/windows-users-permissions.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/sna/docs/windows-users-permissions.html](https://yasirbhutta.github.io/sna/docs/windows-users-permissions.html)

### Lab Task 1: Create a New User with Limited Permissions on Windows
**Objective:**  Create a new user account on a Windows system with restricted access (limited permissions).

1. **Step 1: Open Control Panel**
   - Open the Start menu and type "Control Panel" in the search bar. Click on it.
   
2. **Step 2: Navigate to User Accounts**
   - In the Control Panel, go to **User Accounts**.
   - Click on **Manage another account**.

3. **Step 3: Add a New User**
   - Select **Add a new user in PC settings**.
   - In the settings, go to **Family & other users**.
   - Under **Other users**, click **Add someone else to this PC**.
   - Choose **I don’t have this person’s sign-in information** if you want to create a local account.
   - Then click on **Add a user without a Microsoft account**.

4. **Step 4: Set Up User Details**
   - Enter the desired **username** and **password** for the new account.
   - Click **Next** to create the account.

5. **Step 5: Change Account Type to Standard User**
   - After creating the account, select it from the **Other users** section.
   - Click **Change account type** and set it to **Standard User** (this ensures limited permissions).
   
6. **Step 6: Log in with the New Account**
   - Log out of the Admin account and log in with the newly created account to verify that the permissions are limited.

### Lab Task 2: Create a Folder on D Drive with Restricted Access
**Objective:** Students will create a folder on the D drive from the Admin account and restrict access to the newly created user.

1. **Step 1: Switch to Admin Account**
   - Ensure you are logged in with an **Admin** account.

2. **Step 2: Create a Folder on D Drive**
   - Navigate to the **D: drive** in **File Explorer**.
   - Right-click on an empty area, select **New**, and then **Folder**.
   - Name the folder (e.g., **RestrictedFolder**).

3. **Step 3: Set Folder Permissions**
   - Right-click on the newly created folder and select **Properties**.
   - Go to the **Security** tab.
   - Click on **Edit** under the group or user names section.

4. **Step 4: Add the Newly Created User**
   - Click on **Add**, then type in the username of the new user account you created.
   - Click **Check Names** to verify the user, then click **OK**.

5. **Step 5: Deny Access to the Folder**
   - Once the user is added, select the user in the list.
   - Under **Permissions for [user]**, check the **Deny** box for **Full control** (or any other permissions you want to restrict).
   - Click **Apply** and then **OK** to confirm the changes.

6. **Step 6: Test Access**
   - Log out of the Admin account and log in with the newly created user.
   - Navigate to the **D: drive** and try to access the restricted folder. You should receive an error message indicating that access is denied.

### Lab Summary:
- Students should now understand how to create a user with limited permissions on Windows and how to use folder permissions to restrict access to specific files or directories.