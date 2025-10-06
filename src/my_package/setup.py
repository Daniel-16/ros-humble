from setuptools import find_packages, setup

package_name = 'my_package'

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
    maintainer='Daniel Toba',
    maintainer_email='danieloloruntoba681@gmail.com',
    description='ROS2 client libraries',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_node = my_package.my_node:main',
            'talker = my_package.publisher_member_function:main',
            'listener = my_package.subscriber_member_function:main',
        ],
    },
)
