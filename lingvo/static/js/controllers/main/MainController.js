(function () {


    angular.module('lingvo')
        .controller('MainCtrl', function ($scope, $timeout, $mdSidenav, $rootScope, $http, $cookies) {

            var me_url = 'api/1.0/users/me/';
            $scope.toggleLeft = buildDelayedToggler('left');
            $rootScope.markers = [];


            $scope.logout = function () {
                $http.post("/rest-auth/logout/").success(function (data) {
                    delete $http.defaults.headers.common.Authorization;
                    delete $cookies.token;
                    $cookies.remove("csrftoken");
                    window.location = "/";
                }).error(function (data) {

                });


            };

            /**
             * Supplies a function that will continue to operate until the
             * time is up.
             */
            function debounce(func, wait, context) {
                var timer;

                return function debounced() {
                    var context = $scope,
                        args = Array.prototype.slice.call(arguments);
                    $timeout.cancel(timer);
                    timer = $timeout(function () {
                        timer = undefined;
                        func.apply(context, args);
                    }, wait || 10);
                };
            }

            /**
             * Build handler to open/close a SideNav; when animation finishes
             * report completion in console
             */
            function buildDelayedToggler(navID) {
                return debounce(function () {
                    // Component lookup should always be available since we are not using `ng-if`
                    $mdSidenav(navID)
                        .toggle()
                        .then(function () {

                        });
                }, 200);
            }

            function buildToggler(navID) {
                return function () {
                    // Component lookup should always be available since we are not using `ng-if`
                    $mdSidenav(navID)
                        .toggle()
                        .then(function () {

                        });
                }
            }

            $rootScope.$on('$routeChangeStart', function (event, next) {
                for (var i = 0; i < $rootScope.markers.length; i++) {
                    $rootScope.markers[i].setMap(null);
                }
                $rootScope.markers = [];
            });


            $http.get(me_url).success(function (data) {
                $rootScope.user_id = data.user.id;
            }).error(function (data) {

            });

        })
        .controller('LeftCtrl', function ($scope, $timeout, $mdSidenav) {
            $scope.close = function () {
                // Component lookup should always be available since we are not using `ng-if`
                $mdSidenav('left').close()
                    .then(function () {

                    });

            };
        });

})
();
/**
 Copyright 2016 Google Inc. All Rights Reserved.
 Use of this source code is governed by an MIT-style license that can be in foundin the LICENSE file at http://material.angularjs.org/license.
 **/