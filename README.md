# Todo_APP
A Django Todo project for remembering Day to Day tasks 

Overview of the Project
This project is a simple TODO application that allows users to manage tasks. The application has the following key features:

User Authentication: Users must log in to add new tasks. An unauthenticated user trying to access the task creation page will see a "Page Not Found" error. This is enforced using the @login_required decorator in the add_task view.

Task Viewing: Any logged-in user can view tasks added by other users. This feature ensures that tasks are visible to all authenticated users, fostering collaboration and organization within the application.

Note: Only logged-in users can add tasks, while task viewing is accessible to all authenticated users.

