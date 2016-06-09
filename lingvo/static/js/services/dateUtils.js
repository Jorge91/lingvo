(function () {

    angular.module('lingvo').service('DateUtils', function () {
        
        this.transformToRESTyDate = function (date) {
            if (typeof(date) === "undefined")
                return "";
            var yyyy = date.getFullYear().toString();
            var mm = (date.getMonth() + 1).toString(); // getMonth() is zero-based
            var dd = date.getDate().toString();
            return yyyy + '-' + (mm[1] ? mm : "0" + mm[0]) + '-' + (dd[1] ? dd : "0" + dd[0]); // padding
        };

        this.transformToRESTyDateWODays = function (date) {
            if (typeof(date) === "undefined")
                return "";
            var yyyy = date.getFullYear().toString();
            var mm = (date.getMonth() + 1).toString();
            return yyyy + '-' + (mm[1] ? mm : "0" + mm[0]);
        };

        this.transformToInterface = function (date) {
            return new Date(date.substring(0, 4), date.substring(5, 7) - 1, date.substring(8, 10));
        }

    });

})();