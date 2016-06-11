module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({

        pkg: grunt.file.readJSON('package.json'),

        concat: {
            options: {
                separator: ';',
                process: false,
                stripBanners: {
                    block: true
                }
            },
            app: {
                src: [
                    // libs
                    'bower_components/angular/angular.min.js',                     
                    'bower_components/angular-route/angular-route.min.js',
                    'bower_components/angular-cookies/angular-cookies.min.js',
                    'bower_components/angular-translate/angular-translate.min.js',
                    'bower_components/angular-resource/angular-resource.min.js',
                    'bower_components/angular-animate/angular-animate.min.js',
                    'bower_components/angular-messages/angular-messages.min.js',
                    'bower_components/angular-aria/angular-aria.min.js',
                    'bower_components/angular-material/angular-material.min.js',
                    'bower_components/angular-translate/angular-translate.min.js',
                    'bower_components/angular-translate-loader-partial/angular-translate-loader-partial.min.js',
                    'bower_components/angular-translate-loader-static-files/angular-translate-loader-static-files.min.js',
                    'bower_components/angular-material-icons/angular-material-icons.min.js',


                    'bower_components/jquery/dist/jquery.js',
                    'bower_components/bootstrap/dist/js/bootstrap.min.js',
                    'bower_components/ng-file-upload/ng-file-upload-shim.min.js',
                    'bower_components/ng-file-upload/ng-file-upload.min.js',
                    'bower_components/ngmap/build/scripts/ng-map.min.js',
                    'bower_components/sc-date-time/dist/sc-date-time.js',

                    // Application scripts
                    'static/js/app.js',
                    'static/js/services/*.js',
                    'static/js/factories/*.js',
                    'static/js/controllers/*.js',
                    'static/js/controllers/main/*.js',
                    'static/js/controllers/profile/*.js',
                    'static/js/controllers/meeting/*.js',
                    'static/js/directives/*.js',
                    'static/js/filters/*.js',
                    'static/js/authentication/services/*.js',
                    'static/js/authentication/controllers/*.js'

                ],
                dest: 'static/built/app.js'
            },
            login: {
                src: [
                    // libs
                    'bower_components/angular/angular.min.js',

                    // Application scripts
                    'static/js/login.js',
                    'static/js/controllers/login/LoginController.js'

                ],
                dest: 'static/built/login.js'
            },
            style: {
                src: [
                    'bower_components/sc-date-time/dist/sc-date-time.css',
                    'bower_components/angular-material/modules/closure/menu/menu.min.css',
                    'bower_components/angular-material/angular-material.css',
                    'static/styles/style.css'
                ],
                dest: 'static/built/style.css'
            }

        },

        uglify: {
            options: {
                mangle: false
            },
            built: {
                files: {
                    'static/built/app.js': ['static/built/app.js'],
                    'static/built/login.js': ['static/built/login.js']
                }
            },
        },

        less: {
            build: {
                options: {
                    compress: true,
                    yuicompress: true,
                    optimization: 2
                },
                files: {
                    "static/styles/style.css": ["static/styles/style.less"],
                    "static/built/login.css": ["static/styles/login.less"],
                }
            }
        },

        autoprefixer: {
            style: {
                src: 'static/built/style.css',
                dest: 'static/built/style.css'
            }
        },

        watch: {
            less: {
                files: ['static/styles/*.less'],
                tasks: ['less:build'],
                options: {
                    nospawn: true,
                    spawn: false
                }
            },
            json: {
                files: ['static/locate/en.json', 'static/locate/es.json'],
                options: {
                    nospawn: true,
                    spawn: false
                }
            },
            js: {
                files: ['static/js/*.js', 'static/js/**/*.js'],
                tasks: ['concat'],
                options: {
                    nospawn: true,
                    spawn: false
                }
            }
        },

    });

    // Plugins
    grunt.loadNpmTasks('grunt-autoprefixer');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-merge-json');

    // Default task(s).
    grunt.registerTask('default', ['less:build', 'autoprefixer', 'concat', 'watch']);
    grunt.registerTask('prod', ['less:build', 'autoprefixer', 'concat', 'uglify']);

};
