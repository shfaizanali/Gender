(function() {
  var module;

  module = angular.module('controllers', ['directives', 'models', 'services', 'angularFileUpload']);

  module.controller('HelpController', [
    '$scope', function($scope) {
      $scope.help = "Hello This is Help";
    }
  ]);

  module.controller("HomeController", [
    '$scope', '$http', '$upload', function($scope, $http, $upload)
    {

    }
  ]);

  module.controller("ProfileController", [
    '$scope', '$http', '$upload', function($scope, $http, $upload)
    {

    }
  ]);

  module.controller("AddCourseController", [
    '$scope', '$http', 'GetCookieService', function($scope, $http, GetCookieService)
    {

        $scope.languages = {};
        $scope.form = [];
        window.check = $scope;
        $scope.current_index = 1;
        $http({
            url: "http://localhost:8000/languages/",
            method: "GET"
        }).success(function(data){
            $scope.languages = data;
            if($scope.languages && $scope.languages.length > 0){
                $scope.form[0] = 0;
            }
        }).error(function(data){

        });

        $scope.remove = function(id){
            console.log("removed");
            $('#select'+id).remove();
            $('#removeIcon'+id).remove();
            $scope.form.pop();
        };

        $scope.add = function(){
            $scope.form.push(++$scope.current_index);
        };

        $scope.submitSubscribeForm = function(){

           var formData = {};
           formData['fields'] = [];
           $('.selected_language').each(function(){
               formData['fields'].push( $scope.languages[$(this).val()].pk)
               console.log($(this).val());
           });

           $http({
               url: "http://localhost:8000/subscribe/languages/",
               method: "POST",
               headers:{'X-CSRFToken': GetCookieService.getCookie('csrftoken'), 'Content-Type': 'application/x-www-form-urlencoded'},
               data: formData
           }).success(function(data){
                console.log(data);
           }).error(function(data){
                console.log(data);
           });

           return false;
        }

    }
  ]);

  module.controller("SuccessController", [
    '$scope', '$http', '$location', function($scope, $http, $location)
    {
        //return $location.path("/profile");
    }
  ]);


  module.controller("LoginController", [
    '$scope', '$http', '$location', 'GetCookieService', function($scope, $http, $location, GetCookieService)
    {
        $scope.loginForm = {};
        $scope.errors = {};

        $scope.login = function(_event){
            $http({
                url:"http://localhost:8000/account/login/",
                method: "POST",
                headers:{'X-CSRFToken': GetCookieService.getCookie('csrftoken'), 'Content-Type': 'application/x-www-form-urlencoded'},
                data: $.param( $scope.loginForm)
            }).success(function(data, status, headers, config){
                console.log(data);
                return $location.path("/success");
            }).error(function(data, status, headers, config){
                console.log(data);
                $scope.errors = data.errors;
            });
        }
    }
  ]);

  module.controller('SignupController', [
    '$scope', '$http', '$upload', 'GetCookieService', function($scope, $http, $upload, GetCookieService) {

        $scope.rgForm = {};
        $scope.errors = {};

        $scope.onFileSelect = function ($files) {
            $scope.uploadProgress = 0;
            $scope.selectedFile = $files;
        };

        $scope.signup = function(_event){
            var selectedFile;
            if($scope.selectedFile && $scope.selectedFile.length != 0){
                selectedFile = $scope.selectedFile[0]
            }
            $upload.upload({
                url:"http://localhost:8000/account/signup",
                method: "POST",
                headers:{'X-CSRFToken': GetCookieService.getCookie('csrftoken')},
                data: $scope.rgForm,
                file: selectedFile
            }).progress(function (evt) {
                $scope.uploadProgress = parseInt(100.0 * evt.loaded / evt.total, 10);
            }).success(function(data, status, headers, config){
                console.log(data);
                _event.target.outerHTML = data;
            }).error(function(data, status, headers, config){
                console.log(data);
                $scope.errors = data.errors;
            });
        }
    }
  ]);
  

}).call(this);
