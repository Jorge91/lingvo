(function () {

    var app = angular.module('lingvo', [
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
                prefix: 'locate/',
                suffix: '.json'
            });
            $translateProvider.useSanitizeValueStrategy(null);

            $resourceProvider.defaults.stripTrailingSlashes = false;

            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $httpProvider.defaults.withCredentials = true;
            //$httpProvider.interceptors.push('httpErrorInterceptor');
            // Routes
            /*$routeProvider.when('/login', {
                templateUrl: 'views/authentication/login.html',
                isLogin: true
            }).when('/recover', {
                templateUrl: 'views/authentication/recover_password.html',
                isLogin: true
            }).when('/reset/:firstToken/:passwordResetToken/', {
                templateUrl: 'views/authentication/password_reset_confirm.html',
                isLogin: true
             }).when('/user', {
                templateUrl: 'views/authentication/password_change.html',
            }).when('/contracts', {
                templateUrl: 'views/contracts/contract-list.html'
            }).when('/contracts/:id', {
                templateUrl: 'views/contracts/contract-detail.html'
            }).when('/invoices?', {
                templateUrl: 'views/invoices/invoices-list.html'
            }).when('/invoices/:id', {
                templateUrl: 'views/invoices/invoice-detail.html'
            }).when('/tickets?', {
                templateUrl: 'views/tickets/tickets-list.html'
            }).when('/tickets/new/', {
                templateUrl: 'views/tickets/new-ticket.html'
            }).when('/tickets/:id', {
                templateUrl: 'views/tickets/ticket-detail.html'
            }).when('/documents', {
                templateUrl: 'views/documents/documents-list.html'
            }).when('/fees', {
                templateUrl: 'views/fees/fees-list.html'
            }).otherwise({
                redirectTo: '/login'
            });*/
        }

    ]);

    //app.run(function run( $http, $cookies ){
    //    $http.defaults.headers.common['X-CSRFToken'] = $cookies.get('csrftoken');
    //});


})();