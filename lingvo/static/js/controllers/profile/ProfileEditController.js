(function () {

    angular.module('lingvo').controller('ProfileEditCtrl', ['$scope', '$http', 'DateUtils', '$mdDialog', 'Upload',
        function ($scope, $http, DateUtils, $mdDialog, Upload) {

            var me_url = 'api/1.0/users/me/';
            var profile_url = 'api/1.0/profiles/';
            var languages_url = 'api/1.0/languages/';
            var practice_url = 'api/1.0/languages/practice/';
            var speak_url = 'api/1.0/languages/speak/';
            var id = null;

            // Profile fields
            $scope.updateProfile = function () {
                var data = {
                    "description": $scope.edit_profile.description,
                    "genre": $scope.edit_profile.genre,
                    "born_date": DateUtils.transformToRESTyDate($scope.edit_profile.born_date)
                };

                $http.patch(profile_url + id + '/', data).success(function (data) {
                    $scope.profile = data;
                    $scope.edit_profile = {};
                    $scope.edit_profile.description = data.description;
                    $scope.edit_profile.genre = data.genre;
                    $scope.edit_profile.born_date = DateUtils.transformToInterface(data.born_date);

                    id = data.id;
                    $scope.profileForm.$setPristine();
                }).error(function (data) {
                });
            };

            function loadProfile() {
                $http.get(me_url).success(function (data) {
                    $scope.profile = data;
                    $scope.edit_profile = {};
                    $scope.edit_profile.description = data.description;
                    $scope.edit_profile.genre = data.genre;
                    $scope.edit_profile.born_date = DateUtils.transformToInterface(data.born_date);

                    id = data.id;

                }).error(function (data) {

                });
            }


            // File image management
            $scope.$watch('files', function () {
                if ($scope.files != null) {
                    $scope.upload($scope.files);
                }
            });

            $scope.upload = function (file) {
                Upload.upload({
                    url: profile_url + id + '/',
                    method: 'PATCH',
                    data: {
                        picture: file
                    }
                }).then(function (resp) {
                    loadProfile();
                    $mdDialog.hide();
                }, null, function (evt) {
                });

            };

            // Dialog
            $scope.showPrerenderedDialog = function (ev) {
                $mdDialog.show({
                    controller: DialogController,
                    templateUrl: '/static/templates/profile/imageUpload.html',
                    parent: angular.element(document.body),
                    targetEvent: ev,
                    clickOutsideToClose: true
                });
            };


            // Languages management
            function loadLanguages() {
                $http.get(languages_url).success(function (data) {
                    $scope.languages = data;
                }).error(function (data) {

                });
            }

            $scope.getMatches = function (text) {
                text = text.toLowerCase();
                var ret = $scope.languages.filter(function (d) {
                    return d.name.toLowerCase().startsWith(text);
                });
                return ret;
            };

            $scope.addLanguage = function (type) {
                if (type == 'speak') {
                    var data = {
                        user: $scope.profile.user.id,
                        language: $scope.selectedSpeak.id
                    };
                    postLanguage(speak_url, data);

                } else if (type == 'practice') {
                    var data = {
                        user: $scope.profile.user.id,
                        language: $scope.selectedPractice.id
                    };
                    postLanguage(practice_url, data);
                }

            };

            function postLanguage(url, data) {
                $http.post(url, data).success(function (data) {
                    loadProfile();
                    $scope.selectedSpeak = "";
                    $scope.selectedPractice = "";
                    $scope.searchText = "";
                    $scope.searchText2 = "";
                }).error(function (data) {
                });
            }

            $scope.deleteLanguage = function (type, id) {
                if (type == 'speak') {
                    _deleteLanguage(speak_url, id);

                } else if (type == 'practice') {
                    _deleteLanguage(practice_url, id);
                }
            };

            function _deleteLanguage(url, id) {
                $http.delete(url + id + "/").success(function (data) {
                    loadProfile();
                }).error(function (data) {
                });
            }


            /*
             *
             * Init
             *
             * */
            loadProfile();
            loadLanguages();

        }
    ]);


    function DialogController($scope, $mdDialog) {
        $scope.hide = function () {
            $mdDialog.hide();
        };
        $scope.cancel = function () {
            $mdDialog.cancel();
        };
        $scope.answer = function (answer) {
            $mdDialog.hide(answer);
        };
        $scope.closeDialog = function () {
            $mdDialog.hide();
        };
    }

})
();