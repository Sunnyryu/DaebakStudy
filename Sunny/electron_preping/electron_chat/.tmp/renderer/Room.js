"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _react = require("react");

var _react2 = _interopRequireDefault(_react);

var _Message = require("./Message");

var _Message2 = _interopRequireDefault(_Message);

var _NewMessage = require("./NewMessage");

var _NewMessage2 = _interopRequireDefault(_NewMessage);

var _firebaseBrowser = require("firebase/firebase-browser");

var _firebaseBrowser2 = _interopRequireDefault(_firebaseBrowser);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var ROOM_STYLE = {
    padding: "10px 30px"
};

var Room = function (_React$Component) {
    _inherits(Room, _React$Component);

    function Room(props) {
        _classCallCheck(this, Room);

        var _this = _possibleConstructorReturn(this, (Room.__proto__ || Object.getPrototypeOf(Room)).call(this, props));

        _this.state = {
            description: "",
            messages: []
        };
        _this.db = _firebaseBrowser2.default.database();
        _this.handleMessagePost = _this.handleMessagePost.bind(_this);
        return _this;
    }

    _createClass(Room, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            var roomId = this.props.params.roomId;
            // 컴포넌트 초기화 때 채팅방 상세 정보 추출하기

            this.fetchRoom(roomId);
        }
    }, {
        key: "componentWillReceiveProps",
        value: function componentWillReceiveProps(nextProps) {
            var roomId = nextProps.params.roomId;

            if (roomId === this.props.params.roomId) {
                // 채팅방 ID로 변환할 수 없다면 아무 것도 하지 않기
                return;
            }
            if (this.stream) {
                // 메시지 감시 제거하기
                this.stream.off();
            }
            // state 다시 초기화하기
            this.setState({ messages: [] });
            // 채팅방 상세 다시 추출하기
            this.fetchRoom(roomId);
        }
    }, {
        key: "componentDidUpdate",
        value: function componentDidUpdate() {
            var _this2 = this;

            setTimeout(function () {
                // 화면 아래로 스크롤하기
                _this2.room.parentNode.scrollTop = _this2.room.parentNode.scrollHeight;
            }, 0);
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            if (this.stream) {
                // 메시지 감시 제거하기
                this.stream.off();
            }
        }

        // 메시지 투고 처리

    }, {
        key: "handleMessagePost",
        value: function handleMessagePost(message) {
            var newItemRef = this.fbChatRoomRef.child("messages").push();
            // Firebase에 로그인하고 있는 사용자를 투고 사용자로 사용하기
            this.user = this.user || _firebaseBrowser2.default.auth().currentUser;
            return newItemRef.update({
                writtenBy: {
                    uid: this.user.uid,
                    displayName: this.user.displayName,
                    photoURL: this.user.photoURL
                },
                time: Date.now(),
                text: message
            });
        }
    }, {
        key: "fetchRoom",
        value: function fetchRoom(roomId) {
            var _this3 = this;

            // Firebase 데이터베이스에서 채팅방 상세 데이터 참조 추출하기
            this.fbChatRoomRef = this.db.ref("/chatrooms/" + roomId);
            this.fbChatRoomRef.once("value").then(function (snapshot) {
                var _snapshot$val = snapshot.val(),
                    description = _snapshot$val.description;

                _this3.setState({ description: description });
                window.document.title = description;
            });
            this.stream = this.fbChatRoomRef.child("messages").limitToLast(10);
            // 채팅방의 메시지 추가 감시하기
            this.stream.on("child_added", function (item) {
                var _ref = _this3.state || [],
                    messages = _ref.messages;
                // 추가된 메시지를 state에 할당하기


                messages.push(Object.assign({ key: item.key }, item.val()));
                _this3.setState({ messages: messages });
            });
        }
    }, {
        key: "render",
        value: function render() {
            var _this4 = this;

            var messages = this.state.messages;

            return _react2.default.createElement(
                "div",
                { style: ROOM_STYLE, ref: function ref(room) {
                        return _this4.room = room;
                    } },
                _react2.default.createElement(
                    "div",
                    { className: "list-group" },
                    messages.map(function (m) {
                        return _react2.default.createElement(_Message2.default, { key: m.key, message: m });
                    })
                ),
                _react2.default.createElement(_NewMessage2.default, { onMessagePost: this.handleMessagePost })
            );
        }
    }]);

    return Room;
}(_react2.default.Component);

exports.default = Room;