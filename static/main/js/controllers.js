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

  module.controller('SignupController', [
    '$scope', '$upload', function($scope, $upload) {
          function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
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
                url:"/account/signup/",
                method: "POST",
                headers:{'X-CSRFToken': getCookie('csrftoken')},
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
