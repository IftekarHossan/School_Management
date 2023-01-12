{
    'name': "School",
    'author': "Daffodil Computers Ltd",
    'website': "http://www.daffodilvarsity.edu.bd",

    'category': 'erp',
    'version': '1.1',

    # always loaded
    'data': [
        
        #Views
        'views/student.xml',
        'views/teacher.xml',
        'views/section.xml',
        'views/registration.xml',
        'views/course.xml',

        #Security
        'security/ir.model.access.csv',

        #Menu
        'views/menu.xml',

    ],

}
