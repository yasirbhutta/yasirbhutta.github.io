# Windows Server

## Workgroup and Domain

[slides](https://docs.google.com/presentation/d/1pOhaajToy1Ntq0WzpxSZvI8VZ9GILV34C7_bg7fK2hg/edit?usp=sharing)

## Configuring Domain Controllers

[slides](https://docs.google.com/presentation/d/13NWn6b6q4yk97Gnue5RRCWZbuQcxpO-CNEhN5i0PbcM/edit?usp=sharing)

## File Server Resource Manager (FSRM)

To set file quota and screening using File Manager in **Windows Server 2022**, you can use **File Server Resource Manager (FSRM)**, which is a feature in Windows Server that allows you to manage and control file storage. Here's how you can set up file quotas and file screening:

### 1. **Install File Server Resource Manager (FSRM)**
If FSRM is not already installed, you can add it via Server Manager:

1. Open **Server Manager**.
2. Go to **Manage** > **Add Roles and Features**.
3. In the **Add Roles and Features Wizard**, click **Next** until you reach the **Select features** page.
4. Select **File Server Resource Manager**.
5. Complete the wizard and install the feature.

### 2. **Configure File Quotas**
File quotas allow you to limit the amount of space that a user or group can use on a volume or folder.

1. Open **Server Manager**.
2. Go to **Tools** > **File Server Resource Manager**.
3. In the **FSRM** console, go to **Quotas** (under the **Quota Management** section).
4. Right-click on **Quotas** and select **Create Quota**.
5. Choose the path where you want to set the quota (e.g., a specific folder or volume).
6. You can choose to create a **custom quota** or use an **auto apply template**. For a custom quota:
   - Select **Custom quota properties**.
   - Set a quota limit (e.g., 5 GB).
   - Choose the **template** for the quota (e.g., **Deny disk space** or **Warn when quota is exceeded**).
7. Click **OK** to apply the quota.

### 3. **Configure File Screening**
File screening allows you to control which types of files users can save on a file share.

1. In the **FSRM** console, go to **File Screening** (under the **File Screening Management** section).
2. Right-click on **File Screens** and select **Create File Screen**.
3. Choose the path where you want to apply the file screen (e.g., a folder or volume).
4. Select a **file screen template** or create a custom one. For example, you can block certain file types such as executables or video files.
   - For a **custom file screen**:
     - Click **Create a custom file screen**.
     - Choose the file groups (e.g., **Executable files** or **Image files**) you want to block or allow.
5. Choose the action to take when users attempt to save restricted file types:
   - **Deny the file** (block users from saving the file).
   - **Generate an event** (log the action).
6. Click **OK** to apply the file screen.

### 4. **Monitor and Report**
FSRM also allows you to generate reports on file quotas and screening:

1. In the **FSRM** console, go to **Reports** (under **Storage Reports Management**).
2. You can generate reports on quota usage, file screening activity, and more.

This will set up a basic file quota and file screening configuration on your Windows Server 2022. You can fine-tune the settings depending on the specific requirements of your environment.

## Internet Information Services

[slides](https://docs.google.com/presentation/d/1y6Qh6yb10lhbbGJ6fakblV0wIip9pcHqgi59PZMByXA/edit?usp=sharing)

### Task: **Web Server Setup: Creating a Software Directory with Home and Detail Pages**

1. **Create a subfolder named "softwares"** in the webserver directory.
2. **Develop a home page** that displays a list of all available software.
3. For each software, **create individual HTML pages** containing the software's title and description.

## Group Policies

### Understanding Group Policy Processing

[slides](https://docs.google.com/presentation/d/17KbKXBbA0ofvJh6qA6fclImnhv4vQwgLfBY2rna7H98/edit?usp=sharing)

### Configuring Account Policies

[slides](https://docs.google.com/presentation/d/1ZQYYu4V_qhci6V-HJmavnkqK_UdGjlF85YBOjTHWJJI/edit?usp=sharing)

### Configuring Group Policy Settings

[slides](https://docs.google.com/presentation/d/16Q7WF7R2fjsawlMt7k1MNSrE_F2jBlLME6-kKWCMZio/edit?usp=sharing)



