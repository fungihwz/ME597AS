from setuptools import find_packages, setup

package_name = 'task_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hanwei',
    maintainer_email='zhou1013@purdue.edu',
    description='publish_nodeduration',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = task_1.publiser_member_function:main'
        ],
    },
)
