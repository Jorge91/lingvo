(function () {

    angular.module('lingvo').controller('ProfileEditCtrl', ['$scope', '$http', 'DateUtils', '$mdDialog', 'Upload',
        function ($scope, $http, DateUtils, $mdDialog, Upload) {

            var me_url = 'api/1.0/users/me/';
            var profile_url = 'api/1.0/profiles/';
            var id = null;

            /*
             *
             * Profile updating
             *
             * */
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


            /*
             *
             * Init
             *
             * */
            loadProfile();

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