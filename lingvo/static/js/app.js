(function () {

    var app = angular.module('lingvo', [
        'ngMaterial',
        'pascalprecht.translate',
        'ngRoute',
        'ngCookies',
        'ngResource',
        'ngFileUpload'
    ]);


    app.config(['$httpProvider', '$routeProvider', '$translateProvider', '$resourceProvider',
        function ($httpProvider, $routeProvider, $translateProvider, $resourceProvider) {
            var lang = window.navigator.languages ? window.navigator.languages[0] : null;
            lang = lang || window.navigator.language || window.navigator.browserLanguage || window.navigator.userLanguage;
            if (lang.indexOf('-') !== -1)
                lang = lang.split('-')[0];

            if (lang.indexOf('_') !== -1)
                lang = lang.split('_')[0];

            $translateProvider.preferredLanguage(lang);
            $translateProvider.useStaticFilesLoader({
                prefix: 'static/locate/',
                suffix: '.json'
            });
            $translateProvider.useSanitizeValueStrategy(null);

            $resourceProvider.defaults.stripTrailingSlashes = false;

            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $httpProvider.defaults.withCredentials = true;
            //$httpProvider.interceptors.push('httpErrorInterceptor');
            // Routes
            $routeProvider.when('/profile/', {
                templateUrl: '/static/templates/profile/user-profile.html',
            }).when('/profile/:id', {
                templateUrl: '/static/templates/profile/profile-detail.html',
            }).when('/people/', {
                templateUrl: '/static/templates/profile/people.html',
            }).otherwise({
                redirectTo: '/'
            });
        }

    ]);

    app.config(function ($mdThemingProvider) {

        /*var customBackground = {
         '50': '#79d4fd',
         '100': '#60ccfd',
         '200': '#47c4fd',
         '300': '#FFFFFF',
         '400': '#14b4fc',
         '500': '#03A9F4',
         '600': '#0398db',
         '700': '#0286c2',
         '800': '#0275a8',
         '900': '#02638f',
         'A100': '#92dcfe',
         'A200': '#ace4fe',
         'A400': '#c5ecfe',
         'A700': '#015276'
         };

         $mdThemingProvider
         .definePalette('customBackground',
         customBackground);

         $mdThemingProvider.theme('default')
         .primaryPalette('blue-grey')
         .accentPalette('yellow')
         .warnPalette('yellow')
         .backgroundPalette('customBackground');
         */
        $mdThemingProvider.definePalette('white', {
            '50': '#fff',
            '100': '#fff',
            '200': '#fff',
            '300': '#fff',
            '400': '#fff',
            '500': '#fff',
            '600': '#fff',
            '700': '#fff',
            '800': '#fff',
            '900': '#fff',
            'A100': '#fff',
            'A200': '#fff',
            'A400': '#fff',
            'A700': '#fff',
            'contrastDefaultColor': 'light',    // whether, by default, text (contrast)
                                                // on this palette should be dark or light
            'contrastDarkColors': ['50', '100', //hues which contrast should be 'dark' by default
                '200', '300', '400', 'A100'],
            'contrastLightColors': undefined    // could also specify this if default was 'dark'
        });
        
        $mdThemingProvider.theme('panelTheme')
            .primaryPalette('white')
            .backgroundPalette('indigo')
            .dark();


    });

    //app.run(function run( $http, $cookies ){
    //    $http.defaults.headers.common['X-CSRFToken'] = $cookies.get('csrftoken');
    //});


})();