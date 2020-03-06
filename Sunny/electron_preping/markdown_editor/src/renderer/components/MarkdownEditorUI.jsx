import React from "react";
import styles from "./MarkDownEditorUI.css";
import Editor from "./Editor";

export default class MarkDownEditorUI extends React.Component {

    constructor(props) {
        super(props);
        this.state = { text: "" };
        this.onChangeText = this.onChangeText.bind(this);
    }

    onChangeText(e) {
        this.setState({ text: e.target.value });
    }
    render() {
        return (
            <div className={styles.markdownEditor}>
                <Editor className={styles.editorArea}
                value={this.state.text}
                onChange={this.onChangeText}
            />
            </div>
        );
    }
}
